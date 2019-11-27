Doing an Android build:
Phone connected to computer
Go into phone settings/ developer options/ turn on USB debugging/ also stay awake
in Unity Build Settings/ Android/ 32 bit and Development Build/ Build and Run
Build in Unity 2019.2.10f1 *(not 2018)

11/19: touchDirection working: print direction of touch to screen
11/19: testTouch: trying to get accelerometer to control slider, display in text: HAVE WORKING display acceleration to screen.
***Slider not responding/ not connected to acceleration

11/13: ForceSpeed: Greg got accelerometer data to move a ball around

11/08: soundMobile: added accelerometer and button push to playback sound to code, not tested on device yet
11/19: soundMobile: added touch for record/stop and button for playback, not working yet (issues with mapping to button)

11/08: newSoundMobile: Tap button to play sound (no pause), built on Android and working
11/19: 2 buttons, using buttonRecord script, need audiosource (empty) on Buttons
BUT: There is no argument given that corresponds to the required formal parameter 'call' of 'UnityEvent.AddListener(UnityAction)'
11/21: newCubeController script is *supposed* to use touch input to start/ stop a recording, and push a button to play back:
https://github.com/kineticatat/soundToys/blob/master/NewScripts/NewCubeController.cs
11/21: Touch Direction is displayed to screen with this code:
https://github.com/kineticatat/soundToys/blob/master/NewScripts/TouchDirection
11/21: Button tap plays a sound here:
https://github.com/kineticatat/soundToys/blob/master/NewScripts/ButtonTapSound.cs

Next steps: 
11/21 WORKING: get data read out on screen (accelerometer data)::11/19 still working, different format - vector3 data
get accelerometer to control volume:: 11/19 still working, different format - vector3 data
K try accelerometer code and button playback on android build

Notes: 
Accelerometer Roll a Ball in Android: https://answers.unity.com/questions/1321667/roll-a-ball-beginner-tutorial-in-android-controls.html
Microphone playback in real time: https://support.unity3d.com/hc/en-us/articles/206485253-How-do-I-get-Unity-to-playback-a-Microphone-input-in-real-time-
Using Accelerometer in Unity: http://www.theappguruz.com/blog/learn-to-use-accelerometer-in-unity-in-10-mins
Accelerometer input in Unity PC: https://answers.unity.com/questions/1406689/how-to-get-sensoreg-accelerometer-input-from-exter.html
Magnitometer data in unity documentation: https://docs.unity3d.com/ScriptReference/Compass-rawVector.html
Detailed Accelerometer API info: https://docs.unity3d.com/Packages/com.unity.inputsystem@0.9/api/UnityEngine.InputSystem.Accelerometer.html
