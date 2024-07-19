import matplotlib.pyplot as plt
import pandas as pd

from biorhythm_utils import calculate_rhythm_value, calculate_biorhythm, get_current_date

# Define human rhythm cycles (moved from main script)
PHYSICAL_CYCLE = 23
EMOTIONAL_CYCLE = 28
MENTAL_CYCLE = 33

def plot_rhythm_graph(birth_date):
    current_date = get_current_date()

    # Calculate rhythm values
    physical_value, emotional_value, intellectual_value = calculate_biorhythm(birth_date, current_date)

    print("体力节律:", physical_value)
    print("智商节律:", intellectual_value)
    print("情商节律:", emotional_value)
    
    # Set graph parameters

    # Calculate the start and end dates
    start_date = current_date - pd.DateOffset(days=10)
    end_date = current_date + pd.DateOffset(days=20)

    # Create the date range
    date_range = pd.date_range(start=start_date, end=end_date)

    # Set x_values to the date range
    x_values = date_range

    days_since_birth = [(date - birth_date).days for date in x_values]

    y_values_physical = [calculate_rhythm_value(PHYSICAL_CYCLE, days) for days in days_since_birth]
    y_values_mental = [calculate_rhythm_value(MENTAL_CYCLE, days) for days in days_since_birth]
    y_values_emotional = [calculate_rhythm_value(EMOTIONAL_CYCLE, days) for days in days_since_birth]

    # Create and customize the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    label = ax.text(0, 0, "", ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='gray'))

    ax.plot(x_values, y_values_physical, label='physical', color='blue', linestyle='-')
    ax.plot(x_values, y_values_mental, label='mental', color='green', linestyle='--')
    ax.plot(x_values, y_values_emotional, label='emotional', color='red', linestyle='-.')

    ax.set_xlabel('Date(Since Brith))')
    ax.set_ylabel('rthym value')
    ax.set_title('rthym graph')

    # ax.set_xticks(x_values)  # Set tick marks for each day
    # ax.set_xticklabels([f"{day}" for day in x_values])  # Set tick labels

    ax.set_xticks(x_values)  # Set tick marks for each day
    ax.set_xticklabels([day.strftime('%d') for day in x_values])

    ax.set_ylim(-110, 110)  # Set y-axis limits for better visualization
    ax.grid(True)

    ax.legend()  # Show legend
    
    fig.tight_layout()
    plt.show()

# Moved the main program logic to biorhythm_plot.py
if __name__ == '__main__':
    try:
        # birth_date = biorhythm_utils.get_valid_birth_date()

        import datetime
        birth_str = '1991-04-21'
        birth_date = datetime.datetime.strptime(birth_str, "%Y-%m-%d")
        plot_rhythm_graph(birth_date)
    except Exception as e:
        print("An error occurred:", e)
