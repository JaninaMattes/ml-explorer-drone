import pandas as pd
import os

class StatsLogger:
    """ Log all statistical values over the runtime
    """
    def __init__(self) -> None:
        pass

    def write_csv(self):
        pass

    def plot_csv(self):
        pass

    # TODO: Q&A - clarify Stats Wrapper


class StatsPlotter:
    """Plotting collected network statistics as graphs."""
    def __init__(self) -> None:
        pass

    def plot(self):
        pass


class CSVWriter:
    """Log the network outputs via pandas to a CSV file.
    """
    def __init__(self, filename: str):
        self.count = 1
        self.filename = filename

    def __call__(self, data: dict):
        df = pd.DataFrame(data)
        if not os.path.isfile(self.filename):
            df.to_csv(self.filename, header='column_names')
        else: # else it exists so append without writing the header
            df.to_csv(self.filename, mode='a', header=False)