//trying to use touch data to trigger recording and stopping, then button for playback. Still working out issues with button

using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

public class CubeController : MonoBehaviour
{
    //https://forum.unity.com/threads/record-microphone-to-file.415078/
    //https://support.unity3d.com/hc/en-us/articles/206485253-How-do-I-get-Unity-to-playback-a-Microphone-input-in-real-time-
    bool isRecording = true;
    private AudioSource audioSource;
    private Touch theTouch;
    private Vector2 touchStartPosition, touchEndPosition;
    public Button yourButton;

    //temporary audio vector we write to every second while recording is enabled..
    List<float> tempRecording = new List<float>();

    //list of recorded clips...
    List<float[]> recordedClips = new List<float[]>();

    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        //set up recording to last a max of 1 seconds and loop over and over
        audioSource.clip = Microphone.Start(null, true, 1, 44100);
        audioSource.Play();
        //resize our temporary vector every second
        Invoke("ResizeRecording", 1);

        Button btn = yourButton.GetComponent<Button>();
    
    }

    void ResizeRecording()
    {
        if (isRecording)
        {
            //add the next second of recorded audio to temp vector
            int length = 44100;
            float[] clipData = new float[length];
            audioSource.clip.GetData(clipData, 0);
            tempRecording.AddRange(clipData);
            Invoke("ResizeRecording", 1);
        }
    }

    void Update()
    {
        //space key triggers recording to start...
        // if (Input.GetKeyDown("space"))

        //use touch input instead to start/stop recording
        if (Input.touchCount > 0)
        {
            theTouch = Input.GetTouch(0);

            if (theTouch.phase == TouchPhase.Began || theTouch.phase == TouchPhase.Ended)
            {
                isRecording = !isRecording;
                Debug.Log(isRecording == true ? "Is Recording" : "Off");
            }


            if (isRecording == false)
            {
                //stop recording, get length, create a new array of samples
                int length = Microphone.GetPosition(null);

                Microphone.End(null);
                float[] clipData = new float[length];
                audioSource.clip.GetData(clipData, 0);

                //create a larger vector that will have enough space to hold our temporary
                //recording, and the last section of the current recording
                float[] fullClip = new float[clipData.Length + tempRecording.Count];
                for (int i = 0; i < fullClip.Length; i++)
                {
                    //write data all recorded data to fullCLip vector
                    if (i < tempRecording.Count)
                        fullClip[i] = tempRecording[i];
                    else
                        fullClip[i] = clipData[i - tempRecording.Count];
                }

                recordedClips.Add(fullClip);
                audioSource.clip = AudioClip.Create("recorded samples", fullClip.Length, 1, 44100, false);
                audioSource.clip.SetData(fullClip, 0);
                audioSource.loop = true;

            }
            else
            {
                //stop audio playback and start new recording...
                audioSource.Stop();
                tempRecording.Clear();
                Microphone.End(null);
                audioSource.clip = Microphone.Start(null, true, 1, 44100);
                Invoke("ResizeRecording", 1);
            }

        }

        void ButtonPressed()
        {
            //use number keys to switch between recorded clips, start from 1!!
            for (int i = 0; i < 10; i++)
            {
                SwitchClips(i - 1);
            }
        }

        //chooose which clip to play based on number key..
        void SwitchClips(int index)
        {
            if (index < recordedClips.Count)
            {
                audioSource.Stop();
                int length = recordedClips[index].Length;
                audioSource.clip = AudioClip.Create("recorded samples", length, 1, 44100, false);
                audioSource.clip.SetData(recordedClips[index], 0);
                audioSource.loop = true;
                audioSource.Play();
            }
        }


    }
}
