# Hydra Framework Introduction Slides

This repository contains an introductory presentation about the Hydra framework, created using Quarto. These slides are designed to help colleagues and developers understand the basics of Hydra, including its core concepts, features, and how to use it effectively.

## How to Generate Slides with Quarto

1. **Install Quarto**
   If you don’t have Quarto installed, download and install it from the [Quarto website](https://quarto.org/docs/get-started/).

2. **Clone the Repository**

   ```bash
   git clone https://github.com/nkhusainov/demo_hydra_conf.git
   cd demo_hydra_conf
   ```

3. **Render the Slides**
   Run the following command to generate the slides:

   ```bash
   cd slides
   quarto render
   ```

4. **View the Slides**
   Open generated url

## How to run code

> **_NOTE:_**  Insure you have uv package manager installed

1. Install all depependencies using the following command:

   ```bash
   uv sync
   ```

2. Run the example code using the following command:

    ```bash
    cd src/example_1
    uv run python main.py
    ```