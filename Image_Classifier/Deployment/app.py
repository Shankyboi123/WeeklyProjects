import gradio as gr
from fastai.vision.all import *
from PIL import Image

learn = load_learner('model.pkl')

def classify_image(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn.predict(img)
    return {learn.dls.vocab[i]: float(probs[i]) for i in range(len(learn.dls.vocab))}

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=5),
    title="Cat/Dog Breed Classifier",
    description=(
        "Upload a photo of a cat or dog to predict its breed.\n\n"
        "**This model only recognizes the following 37 breeds:**\n\n"
        "**Cats (12 breeds):** Abyssinian, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, "
        "Maine Coon, Persian, Ragdoll, Russian Blue, Siamese, Sphynx\n\n"
        "**Dogs (25 breeds):** American Bulldog, American Pit Bull Terrier, Basset Hound, Beagle, Boxer, "
        "Chihuahua, English Cocker Spaniel, English Setter, German Shorthaired Pointer, Great Pyrenees, "
        "Havanese, Japanese Chin, Keeshond, Leonberger, Miniature Pinscher, Newfoundland, Pomeranian, Pug, "
        "Saint Bernard, Samoyed, Scottish Terrier, Shiba Inu, Staffordshire Bull Terrier, Wheaten Terrier, "
        "Yorkshire Terrier\n\n"
        "Photos of other breeds (e.g. Golden Retriever, German Shepherd) will be force-matched to the "
        "closest known breed, which may be inaccurate."
    )
)

demo.launch()