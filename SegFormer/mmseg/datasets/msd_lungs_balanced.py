from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MSDLungsBalancedDataset(CustomDataset):
    """ADE20K dataset.

    In segmentation map annotation for ADE20K, 0 stands for background, which
    is not included in 150 categories. ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = (
        "no ailment", "ailment")

    PALETTE = [[120, 120, 120], [92, 0, 255]]

    def __init__(self, **kwargs):
        super(MSDLungsBalancedDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=True,
            **kwargs)
