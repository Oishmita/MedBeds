//defining the pins and variables for sensor input and preparing final data for upload
//with the change in no. of beds, only the total_beds macro and piezo[] array for input pins needs to be altered

#define total_beds 4
//headers needed
#include <WiFi.h>
#include <HTTPClient.h>
//network credentials for connection
const char* ssid     = "dlink-1081";
const char* password = "292987e626";

//including Domain name and URL path or IP address with path
const char* serverName = "http://192.168.0.100/medbeds/post-esp-data.php";

//Keeping this API Key value for compatibility with the PHP code written 
//If the apiKeyValue is changed, the PHP file post-esp-data.php also needs to have the same key 
String apiKeyValue = "tPmAT5Ab3j7F9";

int piezo[] = {34, 35, 32, 33};   // the analog pins connected to the piezo sensors of each bed
int val[total_beds];    // array for storing the status of each bed
int beds_occ=0;
int beds_vac;
int i,j,v;
int c=0;    // counter for holding the status of beds for a specified time (loop iterations)

int ledoutput = 2;    // pin connected to board LED
int threshold = 1000;   //setting the threshold for presence of patient

String Department="Cardiology";

//setting up the input and output pins
void setup()
{
  for(i=0; i<total_beds ; i++)
  {
    pinMode(piezo[i], INPUT);
  }   // setting the piezo pins as input
  pinMode(ledoutput, OUTPUT);   // setting board led as output

  for(i=0; i<total_beds; i++)
  {
    val[i]=0;
  }   // initializing the status of each bed as empty (0)
  
  Serial.begin(115200);

  //configuring wifi connection
  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) { 
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());


}

void loop()
{ 
  
  for(j=0; j<total_beds; j++)
  {
    v=analogRead(piezo[j]);  //   stores the reading of each sensor
    if(v >= threshold)
    {
      val[j] = 1;
      digitalWrite(ledoutput, HIGH);
      delay(100);
    }   // checks the status of each bed
        //if the sensor reading is above threshold, the status of each bed is set as full (1) and led blinks giving an indication
    else
    {
      digitalWrite(ledoutput, LOW);
    }   //else led remains off
  }   //for checking the bed status with each loop

  for(j=0; j<total_beds; j++)
  {
    beds_occ=beds_occ+val[j];
  }   //calculating the total beds occupied

  beds_vac=total_beds-beds_occ; //calculating the vacant beds
  
  Serial.print(beds_occ);
  Serial.print("  ");
  Serial.println(beds_vac);


  if(c>99998)
  {       

          //Check WiFi connection status
          if(WiFi.status()== WL_CONNECTED){
          HTTPClient http;
                  
          // Domain name with URL path or IP address with path
          http.begin(serverName);
                  
          // Specify content-type header
          http.addHeader("Content-Type", "application/x-www-form-urlencoded");    
          // Preparing HTTP POST request data
          String httpRequestData = "api_key=" + apiKeyValue + "&Department=" + Department + "&No_of_beds_occ=" + beds_occ + "&No_of_beds_vac=" + beds_vac + "";
          
          Serial.print("httpRequestData: ");
          Serial.println(httpRequestData);
      
          // Send HTTP POST request
          int httpResponseCode = http.POST(httpRequestData);
      
          if (httpResponseCode>0) {
            Serial.print("HTTP Response code: ");
            Serial.println(httpResponseCode);
          }
          else {
            Serial.print("Error code: ");
            Serial.println(httpResponseCode);
          }
          // Free resources
          http.end();    
        }
        else {
          Serial.println("WiFi Disconnected");
        }

        delay(5000);
  } //for uploading data after a while into the database
  
   
  beds_occ=0;   //setting the beds_occ at 0 with every iteration since the val[] array remians unchanged for a specified time
  c++;    //counting the loop iterations


  if(c==100000)
  { 
    for(i=0; i<total_beds; i++)
    {
      val[i]=0;
    }
    c=0;
  }   //setting the status of each bed to empty (0) after a specified time (here, 100000 loop iterations)
  
}
