

class HermesDataset:
    def __init__(self):
        self.width = 500
        self.height = 500

        self.epoch = 5
        self.batch_size = 20

        self.seeds = {
            "training": -1,
            "validation": -1,
            "test": -1
        }

        self.shuffle = {
            "training": True,
            "validation": True,
            "test": True
        }

        self.crop_aspect_rate = {
            "training": True,
            "validation": True,
            "test": True
        }

        self.class_mode = None
        self.follow_links = True

        self.color_mode = 'rgb'
        self.validation_split = 0.25

    def get_target_size(self):
        return (
            self.get_height(),
            self.get_width()
        )

    def get_validation_split(self) -> float:
        return self.validation_split

    def set_validation_split(
            self,
            value: float
    ) -> None:
        self.validation_split = value

    def get_color_mode(self) -> str:
        return self.color_mode

    def set_color_mode(
            self,
            value: str
    ) -> None:
        self.color_mode = value

    def get_channels(self) -> int:
        if 'grayscale' == self.color_mode:
            return 1

        return len(self.color_mode)

    def get_class_mode(self) -> str | None:
        return self.class_mode

    def set_class_mode(
            self,
            value: str | None
    ) -> None:
        self.class_mode = value

    def get_seeds(self) -> dict:
        return self.seeds

    def set_seeds(
            self,
            value: dict
    ) -> None:
        self.seeds = value

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def set_height(
            self,
            value: int
    ) -> None:
        self.height = value

    def set_width(
            self,
            value: int
    ) -> None:
        self.width = value

    def get_batch_size(self) -> int:
        return self.batch_size

    def set_batch_size(
            self,
            value: int
    ) -> None:
        self.batch_size = value

    def get_epoch(self) -> int:
        return self.epoch

    def set_epoch(
            self,
            value: int
    ) -> None:
        self.epoch = value
