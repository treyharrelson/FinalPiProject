#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_PERIOD_MS 10

Adafruit_BNO055 bno = Adafruit_BNO055(55);

unsigned long tnext, tnow;

void setup(void)
{
  Serial.begin(115200);

  /* Initialise the sensor */
  if(!bno.begin())
  {
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  //calibration, not sure if this helps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
  // uint8_t system=0, gyro=0, accel=0, mag = 0;
  // while((system != 3) && (accel != 3))
  // {
    
  //   bno.getCalibration(&system, &gyro, &accel, &mag);
  //   Serial.print("CALIBRATION: Sys=");
  //   Serial.print(system, DEC);
  //   Serial.print(" Gyro=");
  //   Serial.print(gyro, DEC);
  //   Serial.print(" Accel=");
  //   Serial.print(accel, DEC);
  //   Serial.print(" Mag=");
  //   Serial.println(mag, DEC);
  //   delay(100);
  // }
  // Serial.println(""); Serial.println("Calibrated");


  tnext = millis() + 100;
}

void loop(void)
{
  // fetch quaternion, negative
  imu::Quaternion quat = bno.getQuat();
  quat.x() = -quat.x();
  quat.y() = -quat.y();
  quat.z() = -quat.z();

  // fetch linear acceleration (excludes gravity)
  imu::Vector<3> linearaccel = bno.getVector(Adafruit_BNO055::VECTOR_LINEARACCEL);

  // compute earth-referenced acceleration (excludes sensor tilt)
  imu::Vector<3> acc;
  acc[0] = (1-2*(quat.y()*quat.y() + quat.z()*quat.z()))*linearaccel[0] +   (2*(quat.x()*quat.y() + quat.w()*quat.z()))*linearaccel[1] +   (2*(quat.x()*quat.z() - quat.w()*quat.y()))*linearaccel[2];  // rotate linearaccel by quaternion
  acc[1] =   (2*(quat.x()*quat.y() - quat.w()*quat.z()))*linearaccel[0] + (1-2*(quat.x()*quat.x() + quat.z()*quat.z()))*linearaccel[1] +   (2*(quat.y()*quat.z() + quat.w()*quat.x()))*linearaccel[2];
  acc[2] =   (2*(quat.x()*quat.z() + quat.w()*quat.y()))*linearaccel[0] +   (2*(quat.y()*quat.z() - quat.w()*quat.x()))*linearaccel[1] + (1-2*(quat.x()*quat.x() + quat.y()*quat.y()))*linearaccel[2];

  // try to compute veloctity
  static imu::Vector<3> avgacc, vel;
  float avgrate = 0.001;  // slowly compute average acceleration
  float leakage = 0.001;  // slowly leak the velocity integrator towards zero
  for (int n=0; n<3; n++)
  {
    avgacc[n] = avgrate * acc[n] + (1-avgrate) * avgacc[n];
    vel[n] += BNO055_SAMPLERATE_PERIOD_MS/1000.0 * (acc[n] - avgacc[n]) - leakage * vel[n];
  }


// #if 0
//   Serial.print(acc[0]);
//   Serial.print(",");
//   Serial.print(acc[1]);
//   Serial.print(",");
//   Serial.println(acc[2]);
// #endif

  Serial.print(acc[0]);
  Serial.print(",");
  Serial.print(acc[1]);
  Serial.print(",");
  Serial.print(acc[2]);
  Serial.print(",");
  Serial.print(vel[0]);
  Serial.print(",");
  Serial.print(vel[1]);
  Serial.print(",");
  Serial.println(vel[2]);

  tnow = millis();
  delay(tnext - tnow);
  tnext += BNO055_SAMPLERATE_PERIOD_MS;
}
