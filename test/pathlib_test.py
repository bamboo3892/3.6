from pathlib import Path

p = Path(__file__).parent.parent.joinpath(
    "images", "icon_dog.png").absolute()

print(p)
