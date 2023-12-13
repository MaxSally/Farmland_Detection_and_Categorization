import re
import random

import matplotlib.pyplot as plt
import pandas as pd


def extract_metrics_validation(line):
    pattern = r'Epoch (\d+)/\d+, Validation Top-1 Accuracy: (\d+\.\d+)%, Top-3 Accuracy: (\d+\.\d+)%, Validation F1 Score: (\d+\.\d+), Validation Loss: (\d+\.\d+)'

    # Use re.match to find the pattern in the line
    match = re.match(pattern, line)

    if match:
        epoch = int(match.group(1))
        top1_accuracy = float(match.group(2))
        top3_accuracy = float(match.group(3))
        f1_score = float(match.group(4))
        validation_loss = float(match.group(5))

        return {
            'epoch': epoch,
            'top1_accuracy': top1_accuracy,
            'top3_accuracy': top3_accuracy,
            'f1_score': f1_score,
            'loss': validation_loss
        }
    else:
        return None


def extract_metrics_test(line):
    # Define a regular expression pattern to extract metrics
    pattern = r'Epoch (\d+)/\d+, Test Top-1 Accuracy: (\d+\.\d+)%, Top-3 Accuracy: (\d+\.\d+)%, Test F1 Score: (\d+\.\d+), Test Loss: (\d+\.\d+)'

    # Use re.match to find the pattern in the line
    match = re.match(pattern, line)

    if match:
        epoch = int(match.group(1))
        top1_accuracy = float(match.group(2))
        top3_accuracy = float(match.group(3))
        f1_score = float(match.group(4))
        loss = float(match.group(5))

        return {
            'epoch': epoch,
            'top1_accuracy': top1_accuracy,
            'top3_accuracy': top3_accuracy,
            'f1_score': f1_score,
            'loss': loss
        }
    else:
        return None


metrics = {
    'validation_top1': [],
    'validation_top3': [],
    'validation_f1': [],
    'validation_loss': [],
    'test_top1': [],
    'test_top3': [],
    'test_f1': [],
    'test_loss': []
}

with open('../result/objective3_crop_classification/training_history.txt', 'r') as file:
    lines = file.readlines()

coin = 0

for line in lines:
    if coin == 0:
        metrics_data = extract_metrics_validation(line)
        metrics['validation_top1'].append(metrics_data['top1_accuracy'])
        metrics['validation_top3'].append(metrics_data['top3_accuracy'])
        metrics['validation_f1'].append(metrics_data['f1_score'])
        metrics['validation_loss'].append(metrics_data['loss'])
        # if metrics_data:
        #     print("Extracted Metrics:")
        #     print(f"Epoch: {metrics_data['epoch']}")
        #     print(f"Top-1 Accuracy: {metrics_data['top1_accuracy']}%")
        #     print(f"Top-3 Accuracy: {metrics_data['top3_accuracy']}%")
        #     print(f"F1 Score: {metrics_data['f1_score']}")
        #     print(f"Validation Loss: {metrics_data['loss']}")
        # else:
        #     print("No match found in the text line.")

        coin = 1
    else:
        metrics_data = extract_metrics_test(line)
        metrics['test_top1'].append(metrics_data['top1_accuracy'])
        metrics['test_top3'].append(metrics_data['top3_accuracy'])
        metrics['test_f1'].append(metrics_data['f1_score'])
        metrics['test_loss'].append(metrics_data['loss'])
        # if metrics_data:
        #     print("Extracted Metrics:")
        #     print(f"Epoch: {metrics_data['epoch']}")
        #     print(f"Top-1 Accuracy: {metrics_data['top1_accuracy']}%")
        #     print(f"Top-3 Accuracy: {metrics_data['top3_accuracy']}%")
        #     print(f"F1 Score: {metrics_data['f1_score']}")
        #     print(f"Test Loss: {metrics_data['loss']}")
        # else:
        #     print("No match found in the text line.")
        coin = 0


def plot_metrics(metrics, title):
    df = pd.DataFrame(metrics)

    window_size = 5
    df['validation_top1_ma'] = df['validation_top1'].rolling(window=window_size).mean()
    df['validation_top3_ma'] = df['validation_top3'].rolling(window=window_size).mean()
    df['validation_f1_ma'] = df['validation_f1'].rolling(window=window_size).mean()
    df['validation_loss_ma'] = df['validation_loss'].rolling(window=window_size).mean()

    df['test_top1_ma'] = df['test_top1'].rolling(window=window_size).mean()
    df['test_top3_ma'] = df['test_top3'].rolling(window=window_size).mean()
    df['test_f1_ma'] = df['test_f1'].rolling(window=window_size).mean()
    df['test_loss_ma'] = df['test_loss'].rolling(window=window_size).mean()

    epochs = range(1, len(df['validation_top1_ma']) + 1)

    plt.figure(figsize=(15, 5))

    plt.subplot(2, 2, 1)
    plt.plot(epochs, df['validation_top1_ma'], label='Validation Top-1 Accuracy')
    plt.plot(epochs, df['test_top1_ma'], label='Test Top-1 Accuracy')
    plt.title('Top-1 Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.ylim(0, 100)

    plt.subplot(2, 2, 2)
    plt.plot(epochs, df['validation_top3_ma'], label='Validation Top-3 Accuracy')
    plt.plot(epochs, df['test_top3_ma'], label='Test Top-3 Accuracy')
    plt.title('Top-3 Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.ylim(0, 100)

    plt.subplot(2, 2, 3)
    plt.plot(epochs, df['validation_f1_ma'], label='Validation F1 Score')
    plt.plot(epochs, df['test_f1_ma'], label='Test F1 Score')
    plt.title('F1 Score')
    plt.xlabel('Epoch')
    plt.ylabel('F1 Score')
    plt.legend()
    plt.ylim(0, 1)

    plt.subplot(2, 2, 4)
    plt.plot(epochs, df['validation_loss_ma'], label='Validation Loss')
    plt.plot(epochs, df['test_loss_ma'], label='Test Loss')
    plt.title('Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.ylim(0, 3)

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


plot_metrics(metrics, title='Metrics Over Epochs')
