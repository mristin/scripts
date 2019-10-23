#!/usr/bin/env python3

"""View and rename files in-place."""

import argparse
import os
import pathlib
import shutil
import subprocess
import tempfile
import tkinter as tk
from typing import List, Optional

import PIL.Image
import PIL.ImageTk
import icontract
import logthis


def first_page(path: pathlib.Path) -> PIL.Image:
    """
    Render the first page of the document.

    The caller is responsible to close the image.
    """
    if path.suffix == '.pdf':
        with tempfile.NamedTemporaryFile(suffix='.png') as tmp:
            subprocess.check_call([
                'convert',
                '-density', '100',
                '-resize', '90%',
                '{}[0]'.format(path),
                tmp.name])
            image = PIL.Image.open(tmp.name)

            return image
    else:
        return PIL.Image.open(path.as_posix())


class Model:
    """Represent the global model of the application."""

    @icontract.require(lambda paths: len(paths) > 0, "at least one path")
    def __init__(self, paths: List[pathlib.Path]) -> None:
        self.paths = paths
        self.current_index = 0

    def current(self) -> pathlib.Path:
        """Get the current path."""
        return self.paths[self.current_index]


class Controler:
    """Effect changes."""

    def __init__(self, model: Model) -> None:
        self.model = model

    def rename(self, new: pathlib.Path) -> None:
        """Rename the current viewed file."""
        if new == self.model.current():
            return

        new.parent.mkdir(exist_ok=True, parents=True)
        old = self.model.paths[self.model.current_index]
        shutil.move(old.as_posix(), new.as_posix())

        logthis.say("Moved: {} to {}".format(old, new))

        self.model.paths[self.model.current_index] = new

    def next(self) -> None:
        """Move to the next document."""
        self.model.current_index += 1
        if self.model.current_index == len(self.model.paths):
            self.model.current_index = 0

    def prev(self) -> None:
        """Move to the previous document."""
        self.model.current_index -= 1
        if self.model.current_index < 0:
            self.model.current_index = len(self.model.paths) - 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files", nargs='+', help="list of files to rename",
        required=True)
    args = parser.parse_args()

    paths = [pathlib.Path(file) for file in args.files]

    model = Model(paths=paths)
    controler = Controler(model=model)

    root = tk.Tk()

    new = tk.StringVar()
    new.set(model.current())

    input = tk.Entry(root, textvariable=new)
    input.pack(fill='x')

    def select() -> None:
        """Select the part of the path up to the file name."""
        pth = model.current().as_posix()
        parent, basename = os.path.split(pth)
        stem, ext = os.path.splitext(basename)

        if len(parent) > 0:
            start = len(parent) + len(os.path.sep)
        else:
            start = 0

        if len(ext) > 0:
            end = len(pth) - len(ext)
        else:
            end = len(pth)

        if end > 0:
            input.icursor(end)
        else:
            input.icursor(1)

        input.select_range(start, end)

    photo_label = tk.Label(root)
    photo_label.pack(fill=tk.BOTH, expand=tk.YES)

    # Keep the view of the document as a global variable to prevent
    # garbage collector from collecting it.
    original_image = None  # type: Optional[PIL.Image]
    image = None  # type: Optional[PIL.Image]
    photo = None  # type: Optional[PIL.ImageTk.PhotoImage]

    def draw() -> None:
        """Redraw the document on the photo label."""
        nonlocal image
        nonlocal photo

        assert original_image is not None, \
            "Expected original_image before redrawing the photo label."

        width = photo_label.winfo_width()
        height = photo_label.winfo_height()

        image = original_image.copy()
        image.thumbnail((width, height), PIL.Image.ANTIALIAS)

        photo = PIL.ImageTk.PhotoImage(image=image)
        root.photo_for_gc = photo
        photo_label.configure(image=photo)

    def refresh() -> None:
        """Update the view and input for the current document."""
        nonlocal original_image

        new.set(model.current())
        input.focus_set()
        select()

        original_image = first_page(model.current())

    def on_resize(event: tk.Event) -> None:
        """Handle photo label resize reconfiguration."""
        draw()

    photo_label.bind('<Configure>', on_resize)

    def go_next() -> None:
        """Action the next document."""
        nonlocal new
        controler.rename(new=pathlib.Path(new.get()))
        controler.next()
        refresh()
        draw()

    def go_prev() -> None:
        """Action the previous document."""
        nonlocal new
        controler.rename(new=pathlib.Path(new.get()))
        controler.prev()
        refresh()
        draw()

    def on_enter(event: tk.Event) -> None:
        """Handle enter key press."""
        go_next()

    def on_page_down(event: tk.Event) -> None:
        """Handle page down key press."""
        go_next()

    def on_page_up(event: tk.Event) -> None:
        """Handle page up key press."""
        go_prev()

    root.bind('<Return>', on_enter)
    root.bind('<Prior>', on_page_up)
    root.bind('<Next>', on_page_down)
    refresh()

    def on_click(event: tk.Event) -> None:
        """Handle clicks on the photo."""
        subprocess.check_call(['evince', model.current().as_posix()])

    photo_label.bind('<Button-1>', on_click)

    root.title("viewmove")
    root.geometry('1000x1000')

    root.mainloop()


if __name__ == "__main__":
    main()
