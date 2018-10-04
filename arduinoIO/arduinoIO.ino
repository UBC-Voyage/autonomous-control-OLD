#include "motor.h"
#include "rudder.h"
#include "pins.h"

#define GPSSERIAL Serial1

Motor motor;
Rudder rudder;

// GPS code
// =========================================

char tmp;
char NMEAbuf[82];
char NMEAbuf = 0;

void setup() {
  Serial.begin(9600);
  delay(500);
  Serial.println("Starting...");

  motor.begin(MOTOR_ESC_PIN);
  rudder.begin(RUDDER_SERVO_PIN);

  GPSSERIAL.begin(115200, SERIAL_8N1);

}

void loop() {
  delay(2500);
}

void serialEvent1() {
  while(GPSSERIAL.available()) {
    if(NMEAbuf[NMEAbuf_pointer++] = GPSSERIAL.read())
      parseNMEA();
  }
}

void parseNMEA(char nmea[82]) {
  sscanf(NMEAbuf, "%[$!]%2s%3s%*[^*]*%2x", start_delimiter, message_talker, message_id, checksum);

  switch(message_id) {
    case "GLL": sscanf(NMEAbuf, "$GPGLL%lf,%c,%lf,%c,%2i%2i%5f,%*[AV],%c*%x",); break; //read NMEA 0183 GLL string
    default:
  }
}
