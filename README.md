# my_calculator

# Calculator Historic

## Installation

To use the Calculator Historic, follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-username/calculator-historic.git
```
2. Navigate to the project directory:
```
cd calculator-historic
```
3. Ensure you have Python 3 installed on your system.

## Usage

The Calculator Historic is a command-line application that allows you to perform basic arithmetic operations and save the history of your calculations.

To use the calculator, run the following command:
```
python calculator_historic.py
```

This will start the calculator and display the main menu. You can choose from the following options:

1. Delete the history
2. View the history
3. Save the history to a text file
4. Use the calculator
5. Restore the history
6. Quit

Follow the prompts to perform the desired action.

## API

The `calculator_historic.py` file provides the following functions:

- `initialiser_fichier_json(fichier_json, cle_historique)`: Initializes the JSON file with a basic structure if it doesn't exist.
- `sauvegarder_historique_avant_suppression(fichier_json, cle_historique, fichier_sauvegarde)`: Saves the history to a backup file before deleting it.
- `supprimer_historique(fichier_json, cle_historique, fichier_sauvegarde)`: Deletes the history and saves a backup.
- `restaurer_historique(fichier_json, cle_historique, fichier_sauvegarde)`: Restores the history from the backup file.
- `voir_historique(fichier_json, cle_historique)`: Displays the history.
- `sauvegarder_historique_txt(fichier_json, cle_historique, repertoire_txt, fichier_txt)`: Saves the history to a text file.
- `calculatrice(fichier_json, cle_historique)`: Runs the calculator and saves the calculations to the history.
- `menu()`: Displays the main menu and handles user input.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests for this project, you can use the following command:
```
python -m unittest discover tests
```
This will run all the test cases located in the `tests` directory.
