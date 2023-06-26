# TaxiApp

![TaxiApp](taxi.jpg)

TaxiApp is an interactive tool that simulates the operation of a taximeter used in taxi services. With this application, users can calculate and visualise the cost of a journey based on the distance travelled and the duration of the journey.

The application uses an algorithm to determine the exact fare for the journey, taking into account both the distance travelled and the duration of the journey. The fare is automatically adjusted according to the status of the taxi, whether it is stopped or in motion. In addition, it offers flexible configuration options such as a per-kilometre fare or a reduced fare while the vehicle is stationary.

It also keeps a record of the history of journeys made, including details such as date, time, distance and corresponding fare. This allows users to keep track of their income and trips.

## Installation

Follow the instructions to start the application

```
git clone https://github.com/AI-School-F5-P2/TaxiApp.git
```

## Usage

- [Start the taximeter](/Docs/DOCS.md#start-the-taximeter)
- [Change password](/Docs/DOCS.md#change-password)
- [Change fare prices](/Docs/DOCS.md#change-fare-prices)
- [View trip history](/Docs/DOCS.md#view-trip-history)
- [Download trip history](/Docs/DOCS.md#download-trip-history)
- [Delete trip history](/Docs/DOCS.md#delete-trip-history)
- [Update Database](/Docs/DOCS.md#update-database)
- [Perform tests](/Docs/DOCS.md#perform-tests)
- [View graph call](/Docs/DOCS.md#view-graph-call)

## Run tests

To run tests, run the following command

```
  pytest
```

## View help

To view help, run the following command

```
  python App.py --help
```

## Work Tree

```

Taxi_Fork
├─ .editorconfig
├─ App.py
├─ Controllers
│ ├─ AuxFunctions.py
│ ├─ ControlHistory.py
│ ├─ ControlTravel.py
│ ├─ Fees.py
│ ├─ LoginAuth.py
│ ├─ Navigate.py
│ └─ Prices.py
├─ Models
│ └─ DataTrip.py
├─ Pipfile
├─ Pipfile.lock
├─ README.md
├─ Views
│ ├─ Documentation.py
│ ├─ MainTaxi.py
│ ├─ NewPrices.py
│ ├─ Options.py
│ ├─ PrintValues.py
│ ├─ Timer.py
│ └─ Welcome.py
├─ config_manager.py
├─ storytime
│ ├─ 1306-1.png
│ ├─ 1306-2.png
│ ├─ 1306-3.png
│ └─ 1306.png
└─ taxi.jpg

```

## Authors

- [@kamilodev](https://github.com/kamilodev)
- [@luisdavidtribino](https://github.com/luisdavidtribino)

<br>

## 🛠 Skills

![Language](https://img.shields.io/badge/Language-Python-red?logo=python&logoColor=white&color=green)&nbsp;&nbsp;
![Git](https://img.shields.io/badge/Git-red?logo=git&logoColor=white&color=red)&nbsp;&nbsp;
![GitHub](https://img.shields.io/badge/GitHub-red?logo=github&logoColor=white&color=black)&nbsp;&nbsp;
![MongoDB](https://img.shields.io/badge/MongoDB-green?logo=mongodb&logoColor=white&color=green)&nbsp;&nbsp;
![pytest](https://img.shields.io/badge/pytest-purple?logo=pytest&logoColor=white&color=purple)&nbsp;&nbsp;
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-blue?logo=visual-studio-code&logoColor=white&color=blue)&nbsp;&nbsp;
![GNU Bash](https://img.shields.io/badge/GNU%20Bash-orange?logo=gnu-bash&logoColor=white&color=orange)

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
