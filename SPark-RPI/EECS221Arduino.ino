int timer = 0;

void setup() {
  //Initialization 
  pinMode(D0, OUTPUT);  //Built-in LED
  pinMode(D6, OUTPUT);  //Left LED

  Serial.begin(9600);
}

void loop() {
  Serial.println("EECS221 HW1 Part1");
  while(1)
  {
    int lightSensor = analogRead(A0);
    //Serial.print("The sensor value is:"); 
    Serial.println(lightSensor);  //Print sensor values
    delay(500);
    /*
    if (lightSensor <= 300)
    {
      digitalWrite(D6, LOW);

    }
    else if (lightSensor > 300 && lightSensor <= 650)
    {
      digitalWrite(D6, HIGH);
      
    }
    else if (lightSensor > 650)
    {
      digitalWrite(D6, HIGH);

    }
    delay(500);  //Read sensor values every 0.5s
    timer = timer + 1;
    if(timer >= 600)
    {
      timer = 0;
      break;
    }
    */
  }/*
  Serial.println("Average Part");
  while(1)
  {
    int average = 0;
    int lightSensor = analogRead(A0);
    for (int i = 0; i < 6; i++){
        lightSensor = lightSensor + analogRead(A0);
        delay(500);
    }
    average = lightSensor / 6;
    Serial.print("The average sensor value from the last 3s is:"); Serial.println(average);
    if (average <= 300){
      digitalWrite(D6, LOW);  
    }
    else if (average > 300 && average <= 650){
      digitalWrite(D6, HIGH);  
    }
    else if (average > 650){
      digitalWrite(D6, HIGH);
    }
    timer = timer + 1;
    if(timer > 11){
      timer = 0;
      break;
    }
  }
  */
}
