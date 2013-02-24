from i3pystatus.file import File

class Backlight(File):
    """
    Screen backlight info

    Available formatters:
    * brightness
    * max_brightness
    * percentage
    """

    settings = (
        ("format", "format string"),
        ("backlight", "backlight, see `/sys/class/backlight/`"),
        "color",
    )
    required = ()

    backlight="acpi_video0"
    format="{brightness}/{max_brightness}"

    interval=5
    base_path = "/sys/class/backlight/{backlight}/"
    components={
        "brightness": (int, "brightness"),
        "max_brightness": (int, "max_brightness"),
    }
    transforms={
        "percentage": lambda cdict: (cdict["brightness"] / cdict["max_brightness"]) * 100,
    }

    def init(self):
        self.base_path = self.base_path.format(backlight=self.backlight)

        super().init()