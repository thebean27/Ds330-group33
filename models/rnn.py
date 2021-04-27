from tensorflow.keras.models import Sequential

class Rnn:

    def __init__(self):
        self.model = Sequential()

    def build_model(self):
        pass

    def train(self, x_train, y_train, epochs=8, batch_size=32):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=2)

    def predict(self, x):
        return self.model.predict(x)
