#include <wiringPi.h>
#include <stdio.h>
#define RED_LED_PIN 9
#define YELLOW_LED_PIN 8
#define GREEN_LED_PIN 7
int main (void){
    wiringPiSetupGpio();
    pinMode (RED_LED_PIN, OUTPUT);
    pinMode (YELLOW_LED_PIN, OUTPUT);
    pinMode (GREEN_LED_PIN, OUTPUT);

    digitalWrite (RED_LED_PIN, HIGH);
    delay(2000);
    digitalWrite (RED_LED_PIN, LOW);
    digitalWrite (YELLOW_LED_PIN, HIGH);
    delay(2000);
    digitalWrite (YELLOW_LED_PIN, LOW);
    digitalWrite (GREEN_LED_PIN, HIGH);
    delay(2000);
    digitalWrite (GREEN_LED_PIN, LOW);

    pinMode (RED_LED_PIN, INPUT);
    pinMode (YELLOW_LED_PIN, INPUT);
    pinMode (GREEN_LED_PIN, INPUT);

    return 0;
}