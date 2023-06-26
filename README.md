Summer Internship Microservice
This repository contains a Flask microservice for predicting total, ht, base ht, and tva values from JSON text input. 
The microservice uses a machine learning model trained on a dataset of text inputs and corresponding output values.


Installation
Clone the repository:


git clone https://github.com/Ahmed-cherif/summer_intership-microservice.git
Install the required dependencies:



pip install -r requirements.txt
Run the microservice:


python app.py



{
  "text": "dar djerba commande n 016 du 12/04/2023 1952 a emporter x rebes complet tie 2 total euros 53 og cb 53.00 faux base ht tva 10.00 48.18 4.82 il",
  "entities": [
    {
      "start": 100,
      "end": 105,
      "label": "TOTAL"
    },
    {
      "start": 129,
      "end": 134,
      "label": "TVA"
    },
    {
      "start": 135,
      "end": 140,
      "label": "TOTALHT"
    }
  ]
}

The microservice will return a JSON response with the predicted values:


{
  "total": 53.0,
  "ht": 48.18,
  "base_ht": 53.0,
  "tva": 4.82
}
Model Training

To train the model, follow these steps:


Prepare a dataset in Excel format with two columns: "text" (input) and "total", "ht", "base ht", "tva" (output).

Modify the train_model.py script to load your dataset and configure the training process.


Contributing
Contributions to this project are welcome. Feel free to open an issue or submit a pull request.
