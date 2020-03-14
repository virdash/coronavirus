# 2019 Novel Coronavirus

Wednesday 29th January 2020, the Novel Coronavirus was declared a Global Health Emergency by the World Health Organisation [(WHO)](https://www.who.int/emergencies/diseases/novel-coronavirus-2019 'World Health Organisation'). On the 7th February 2020 the number of confirmed cases was 31,485 in over 28 countries, which rose to 71,811 by 17th February 2020 (ie over 128% in 10 days).

This project is to build an information hub for the 2019 novel coronavirus. This hub will contain interactive dashboard that gives a real-time visualization on the coronavirus and up-to-date information on its prevention.

[![Corona Virus](http://img.youtube.com/vi/mOV1aBVYKGA/0.jpg)](http://www.youtube.com/watch?v=mOV1aBVYKGA "source: World Health Organisation")

## Table of contents

- [Getting Started](#getting-started)
- [Technology](#technology)
  - [Prerequisites](#prerequisite)
  - [Built With](#built-with)
  - [Installing](#installing)
- [How to Contribute](#how-to-contribute)
- [Acknowledgement](#acknowledgment)
  - [Inspiration](#inspiration)
  - [Data Source](#resource)
- [License](#license)

## Getting Started

These instructions will get a copy of the project up and running on your local machine for development and testing purposes. See ['how to contribute'](#how-to-contribute) for notes on contributing to the project.

## Technology

The following software needs to be installed.

### Prerequisite

- [Python 3.5 and later](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Other dependencies](./requirements.txt)
- [Google Cloud Platform](https://cloud.google.com/)

### Built With

- [Plotly-dash](https://dash.plot.ly/)
- [Flask](https://palletsprojects.com/p/flask/)

### Installing

**Create a virtual environment.**
Use **virtualenv** to create a virtual environment for the project, Run the following in your terminal.

1. Install virtualenv using pip3.
  ```pip3 install virtualenv```

2. In the root of the project, create a virtual environment.
  ```virtualenv workspace```

3. Activate workspace.
  ```source/workspace/bin/activate```

**Install the dependences**
Run the requirements.txt on the activated workspace
  ```pip install -r requirements.txt```

**Run the application server**
Run main.py in the app folder

  ```python main.py```

## How to contribute

You can contribute to the project and make it better. It is an open source project. Improve the code and send in a pull request with your contributions.

[Here is how to send in a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

If sending pull requests are not your thing, you can send me a tweet @SolomonIgori or email at [igorisolomon@gmail.com](igorisolomon@gmail.com "Igori's email")

## Acknowledgment

### Inspiration

- [Johns Hopkins University Dashboard](https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html?fbclid=IwAR2mWEw0X_B5jbR0Fm23t2TVJGzVqUY6ok98DzrGLMrMXCR_c5joZV5AdNU#/bda7594740fd40299423467b48e9ecf6)

### Resource

- [World Health Organization (WHO)](https://www.who.int/)
- [Observable](https://observablehq.com/@fil/ncov2019-data)
- [Johns Hopkins University Data Source](https://github.com/CSSEGISandData/COVID-19)

## License

The project is licensed under the MIT license. See [LICENSE.md](https://github.com/igorisolomon/coronavirus/blob/master/LICENSE 'MIT License') for more information.
