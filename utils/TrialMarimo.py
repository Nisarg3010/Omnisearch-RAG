# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.8",
# ]
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    print("Greetings, world!")
    return


if __name__ == "__main__":
    app.run()
