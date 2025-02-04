import math

class NaiveBayesClassifier:
    def __init__(self):
        self.classes = None
        self.prior_probs = {}
        self.conditional_probs = {}
    
    def fit(self, X, y):
        self.classes = set(y)  # Get unique classes
        total_samples = len(y)
        feature_count = len(X[0])
        
        # Calculate prior probabilities P(class)
        for c in self.classes:
            self.prior_probs[c] = sum(1 for label in y if label == c) / total_samples
        
        # Calculate conditional probabilities P(feature|class)
        self.conditional_probs = {c: [{} for _ in range(feature_count)] for c in self.classes}
        
        for c in self.classes:
            class_samples = [X[i] for i in range(total_samples) if y[i] == c]
            class_count = len(class_samples)
            
            for j in range(feature_count):
                feature_values = [sample[j] for sample in class_samples]
                unique_values = set(feature_values)
                
                for val in unique_values:
                    self.conditional_probs[c][j][val] = (feature_values.count(val) + 1) / (class_count + len(unique_values))
    
    def predict(self, X_test):
        predictions = []
        for sample in X_test:
            class_probs = {}
            for c in self.classes:
                class_probs[c] = math.log(self.prior_probs[c])
                for j in range(len(sample)):
                    if sample[j] in self.conditional_probs[c][j]:
                        class_probs[c] += math.log(self.conditional_probs[c][j][sample[j]])
                    else:
                        class_probs[c] += math.log(1e-6)  # Small smoothing for unseen values
            predictions.append(max(class_probs, key=class_probs.get))
        return predictions

# Example usage
data = [["Sunny", "Hot", "High", "Weak"],
        ["Sunny", "Hot", "High", "Strong"],
        ["Overcast", "Hot", "High", "Weak"],
        ["Rain", "Mild", "High", "Weak"],
        ["Rain", "Cool", "Normal", "Weak"],
        ["Rain", "Cool", "Normal", "Strong"],
        ["Overcast", "Cool", "Normal", "Strong"],
        ["Sunny", "Mild", "High", "Weak"],
        ["Sunny", "Cool", "Normal", "Weak"],
        ["Rain", "Mild", "Normal", "Weak"],
        ["Sunny", "Mild", "Normal", "Strong"],
        ["Overcast", "Mild", "High", "Strong"],
        ["Overcast", "Hot", "Normal", "Weak"],
        ["Rain", "Mild", "High", "Strong"]]

labels = ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]

# Training the model
nb = NaiveBayesClassifier()
nb.fit(data, labels)

# Testing
test_data = [["Sunny", "Cool", "High", "Strong"],
             ["Overcast", "Mild", "Normal", "Weak"],
             ["Rain", "Mild", "High", "Strong"]]

predictions = nb.predict(test_data)
print("Predictions:", predictions)
