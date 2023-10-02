# Population Growth Analysis

This repository contains Python scripts for analyzing population growth using the discrete-time logistic growth model. It calculates and visualizes the changes in population size, the maximum per capita growth rate, the proportion of carrying capacity remaining unused, the rate of change of the population, and the population size at the start of the next year.

## Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Introduction

Understanding how populations of species change over time is essential in ecological and biological research. This repository provides Python scripts to model and analyze population growth dynamics using the discrete-time logistic growth model. It takes into account parameters such as the maximum per capita growth rate, carrying capacity, and initial population size to simulate and display the changes in population size over multiple years.

## Requirements

- Python 3.x
- `numpy` library
- `prettytable` library (for a visually appealing tabular presentation)

You can install the required libraries using pip:

```bash
pip install numpy prettytable
```


## Usage

1. Clone the repository to your local machine:
   <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/abelxmendoza/PopulationGrowth_Analysis.git
  </code></div></div></pre>
* Navigate to the repository directory:
  <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>
* <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">cd PopulationGrowth_Analysis
  </code></div></div></pre>
* Run the Python script to analyze population growth. For example:
  <pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span></div></div></pre>

1. <pre><div class="bg-black rounded-md mb-4"><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python population_growth_analysis.py
   </code></div></div></pre>

   This script will model population growth based on the provided parameters and display the results in a formatted table.
2. Explore the generated data and use it for further analysis or visualization as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
