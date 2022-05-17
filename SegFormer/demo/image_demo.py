from argparse import ArgumentParser
import matplotlib.pyplot as plt
from glob import glob
import mmcv
from mmseg.apis import inference_segmentor, init_segmentor
from class_names import get_palette
from imageio import imread
import matplotlib.cm as cm
my_cmap = cm.Reds
my_cmap.set_under('k', alpha=0)


def show_result_pyplot(model, img, result, palette=None, fig_size=(15, 10), train_or_test='train'):
    """Visualize the segmentation results on the image.

    Args:
        model (nn.Module): The loaded segmentor.
        img (str or np.ndarray): Image filename or loaded image.
        result (list): The segmentation result.
        palette (list[list[int]]] | None): The palette of segmentation
            map. If None is given, random palette will be generated.
            Default: None
        fig_size (tuple): Figure size of the pyplot figure.
        train_or_test (str): 'train' or 'test'.
    """

    if hasattr(model, 'module'):
        model = model.module
    img = model.show_result(img, result, palette=palette, show=False)
    plt.figure(figsize=fig_size)
    fig, ax = plt.subplots(1, 1, figsize=fig_size)
    ax.imshow(mmcv.bgr2rgb(img), alpha=1.0)
    if train_or_test == 'train':
        img_annot = img.replace("images", "annotations")
        img_annot = imread(img_annot)
        ax.imshow(img_annot, cmap=my_cmap, interpolation='none',
                  clim=[0.9, 1], alpha=.4)
    plt.show()


def main():
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument('--num', help='Number of images to show', type=int)
    parser.add_argument('--train_or_test', help='Number of images to show', default='train', type=str)
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--palette',
        default='cityscapes',
        help='Color palette used for segmentation map')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_segmentor(args.config, args.checkpoint, device=args.device)
    for img in glob(f'{args.img}/*.png')[:args.num]:
        print("Plotting: ", img)
        # test a single image
        result = inference_segmentor(model, img)
        # show the results
        show_result_pyplot(model, img, result, get_palette(args.palette), args.train_or_test)


if __name__ == '__main__':
    main()
