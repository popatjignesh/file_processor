# File Processor


## Overview

The File Processor is a back-end development task designed to read data from multiple `.dat` files located in a specified input folder, process the data, and convert it into an expected CSV file in the output folder. The CSV file includes a header, processed data, and specific salary details.


## Directory Structure
```bash
file_processor/
    input/
    output/
    utils/
        __init__.py
        processor.py
    main.py
    README.md
```

## Input File Format

The input `.dat` files should have the following tab-separated headers:
```bash
id    first_name    last_name    email    job_title    basic_salary    allowances
```


## Output CSV Format

The resulting CSV file will have the following headers:
```bash
id, first_name, last_name, email, job_title, basic_salary, allowances, Gross Salary
```

## How to Use

1. **Clone the Repository**

    Clone the repository to your local machine:

    ```bash
    git clone <repository-url>
    cd file_processor
    ```

2. **Place Input Files**

    Place the `.dat` files inside the `input/` directory.

3. **Run the Processor**

    Execute the `main.py` script to process the files:

    ```bash
    python main.py
    ```

    This will generate the `output.csv` file in the `output/` directory.
