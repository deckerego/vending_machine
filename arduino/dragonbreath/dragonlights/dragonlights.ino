#define GREENPIN  9
#define BLUEPIN   10
#define REDPIN    11
#define BUTTON    12

int buttonState = 0;

void setup() {
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  pinMode(REDPIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);

  analogWrite(GREENPIN, 0);
  analogWrite(BLUEPIN, 0);
  analogWrite(REDPIN, 0);
}

void loop() {
  if(digitalRead(BUTTON) == LOW) {
    digitalWrite(LED_BUILTIN, HIGH);
    for (int i = 0; i <= 255; i += 16) {
      analogWrite(REDPIN, i);
      analogWrite(BLUEPIN, i / 2);
      analogWrite(GREENPIN, i / 2);
      delay(100);
    }

    for (int i = 255; i >= 0; i -= 8) {
      analogWrite(REDPIN, 255);
      analogWrite(BLUEPIN, i / 2);
      analogWrite(GREENPIN, i / 2);
      delay(100);
    }

    delay(5000);

    for (int i = 255; i >= 0; i -= 8) {
      analogWrite(REDPIN, i);
      delay(100);
    }

    analogWrite(GREENPIN, 0);
    analogWrite(BLUEPIN, 0);
    analogWrite(REDPIN, 0);
  }
  digitalWrite(LED_BUILTIN, LOW);
}
