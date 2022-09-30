#define GREENPIN  9
#define BLUEPIN   10
#define REDPIN    11
#define WAITTIME  1000

void setup() {
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  pinMode(REDPIN, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  analogWrite(GREENPIN, 0);
  analogWrite(BLUEPIN, 0);
  analogWrite(REDPIN, 0);
  digitalWrite(LED_BUILTIN, LOW);
  delay(WAITTIME);

  analogWrite(GREENPIN, 255);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(WAITTIME);

  analogWrite(GREENPIN, 0);
  analogWrite(BLUEPIN, 255);
  delay(WAITTIME);

  analogWrite(BLUEPIN, 0);
  analogWrite(REDPIN, 255);
  delay(WAITTIME);
}
