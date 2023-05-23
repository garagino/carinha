#define PIR = 2;
#define led = 3;
int cnt = 0;
int tempo = 0
int estadoPIR = 0;
void setup() {
  pinMode(PIR, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  estadoPIR = digitalRead(PIR);
  if (estadoPIR == HIGH) {
    digitalWrite(led, HIGH);
    delay(1);
    tempo=tempo+1
    Serial.println("Movimentação detectada");
  } 
  else {
    digitalWrite(led, LOW);
    Serial.print("Nenhum movimento detectado");
    if (tempo>=500){
      cnt=cnt+1
    }
    cnt=0
  }
  delay(100);
}


