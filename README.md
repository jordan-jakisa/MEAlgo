# Gale-Shapley Algorithm for Stable Marriage Problem

This repository contains an implementation of the Gale-Shapley algorithm, a solution to the stable marriage problem. The algorithm matches N men and N women based on their preferences, ensuring that each person is matched with their highest preference and resulting in a stable match.

## Background

The stable marriage problem arises in various scenarios, such as matching doctors to residency programs or matching partners in relationships. The algorithm is designed to efficiently solve this problem by considering the preferences of individuals and finding an optimal matching.

## Algorithm Overview

The Gale-Shapley algorithm operates in several rounds, with men proposing to their preferred choices and women selecting their favorite among the proposals received. The process continues iteratively until all individuals are matched. The resulting match is always stable, meaning that there are no two individuals who would both prefer each other over their current partners.

## Example and Step-by-Step Explanation

To illustrate the algorithm, let's consider the example of matching four kings and four queens. The algorithm starts with each man proposing to his top choice among the available women. If a woman receives multiple proposals, she chooses her favorite among them. The rejected men proceed to the next round and propose to their next preferred choices. Similarly, women without partners, if receiving multiple proposals, select their favorite from the available options. This process continues until every person is matched, ensuring a stable match.

## Repository Contents

- `gale_shapley.py`: Contains the implementation of the Gale-Shapley algorithm in Python.
- `unit_tests.py`: Provides unit tests to validate the correctness of the algorithm implementation.
- `README.md`: The file you are currently reading, providing an overview of the repository and the algorithm.

## Getting Started

To understand the Gale-Shapley algorithm and its step-by-step execution, please refer to the `gale_shapley.py` file. The code is accompanied by detailed explanations, making it easy to grasp the underlying concepts.

## Running Unit Tests

To ensure the correctness of the implementation, unit tests are provided in the `unit_tests.py` file. These tests validate the algorithm against various scenarios, verifying that it produces the expected results. You can run the unit tests using a Python testing framework of your choice.

## Contribution

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Together, we can enhance the algorithm implementation and expand its applications.

## Acknowledgments

The Gale-Shapley algorithm is a fundamental concept in matching markets and has significant applications in various domains. This repository aims to provide a clear and understandable implementation along with step-by-step explanations and unit tests.
