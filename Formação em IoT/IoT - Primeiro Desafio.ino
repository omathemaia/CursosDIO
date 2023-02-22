int sensorPin = A0; 
int ledPin1 = 8; 
int ledPin2 = 2; 
int ledPin3 = 9; 

void setup() {
  pinMode(ledPin1, OUTPUT); 
  pinMode(ledPin2, OUTPUT); 
  pinMode(ledPin3, OUTPUT); 
  Serial.begin(9600);
}

void loop() {
  int temperatura = analogRead(sensorPin); // realiza a leitura do sensor de temperatura

  float temperaturaC = (5.0 * temperatura * 100.0) / 1024.0; // converte a leitura do sensor em temperatura em graus Celsius

  Serial.print("Temperatura: ");
  Serial.print(temperaturaC);
  Serial.println("°C");

  if (temperaturaC >= 30) { 
    digitalWrite(ledPin1, HIGH); // aciona o LED 1
  } else {
    digitalWrite(ledPin1, LOW); // desliga o LED 1
  }

  if (temperaturaC > 50) { 
    digitalWrite(ledPin2, HIGH); 
    digitalWrite(ledPin3, HIGH); 
  } else {
    digitalWrite(ledPin2, LOW); 
    digitalWrite(ledPin3, LOW); 
  }

  delay(1000); 
}