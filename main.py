# Ship the entry image to the directory make.fun reads from.
# Nothing but the standard library is used and no network
# is touched: the PNG beside this file is read and its
# bytes are written out unchanged, so running the script
# twice leaves two identical files behind.
import os as _os
import pathlib as _pl

_src = _pl.Path(__file__).resolve().parent.joinpath("entry.png")
_dst = _pl.Path(_os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).joinpath("entry.png")
_dst.parent.mkdir(parents=True, exist_ok=True)
_dst.write_bytes(_src.read_bytes())
