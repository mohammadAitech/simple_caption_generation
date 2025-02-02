hello everyone
This project is a <h4><strong>caption production program for virtual space,</h4></strong> which is a beginner level

So let's examine this project step by step together

<h1> 🚀 Getting Started </h1>

<h3>First step:</h3>
<hr>
<h4> 🔧 Installation</h4>
<p>Installing the dependencies of the project, we install the dependencies with the following command</p>
<hr>
```bash
    pip install transformers
    pip install gradio
    pip install torch
```

or perfessionally


```bash
    pip install transformers torch gradio
```

<h3>Second step:</h3>
<hr>
<p>
After installing the dependency, you need to import and use the dependency required by the project.
So, in the code line below, we enter them into the project and use it
</p>

```bash
    import gradio as gr
    from transformers import pipeline
```

<h3>Third step:</h3>
<hr>
<p>
Create a variable and maintain the built model
After this project, we use a model called distilgpt2
</p>

```bash
    caption_generation = pipeline("text-generation", model="distilgpt2")
```

<h3>Fourth step:</h3>
<p>
In this step of the project, we are trying to create a function and give an input to the function 
The function works in such a way that we give a series of settings to the model we made so that we can optimize the model, and then we give the input of the function to this function, after generating the caption, we return it so that we can use it.
</p>

<strong>Code example:</strong>
```bash
    def caption_gen(prompt):
        result = caption_generation(prompt, max_length=50, temperature=0.9, top_k = 50, top_p = 0.9,num_return_sequences=1)
```

<p>In the last step, we create an interface for the project and finish the project</p>

<strong>Code example:</strong>
```bash
    interface = gr.Interface(
        fn=caption_gen,
        inputs=gr.Textbox(lines=2,placeholder="یک کلمه یا یک جمله را وارد کنید."),
        outputs="text",
        title="تولید کپشن برای فضای مجازی",
        description="یک کلمه یا یک جمله وارد کنید تا کپشن جذاب دریافت کنید.",
    )

    interface.launch()
```