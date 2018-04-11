# Image File Split Macro

Macro for separating image files with various multipliers.
**Only works on Pyhton 2**.

## How to use

```
$ python manager.py create
$ python macro.py "BI" "icon_app"

BI@1x.png -> drawable-mdpi/icon_app.png
BI@1.5x.png -> drawable-hdpi/icon_app.png
BI@2x.png -> drawable-xhdpi/icon_app.png
BI@3x.png -> drawable-xxhdpi/icon_app.png
BI@4x.png -> drawable-xxxhdpi/icon_app.png
```

## Be careful!

It converts the files by order of the multiplier (a number after '@' and 'x')

- @1x -> mdpi/
- @1.5x -> hdpi/
- @2x -> xhdpi/
- @3x -> xxhdpi/
- @4x -> xxxhdpi/

This macro is not stable and run immediately, so make sure you have a copy of your image files. (for backup!)
Use only in strictly controlled circumstances.

I'm almost new to Python, so any help or recommendation would be very thankful.
