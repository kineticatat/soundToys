using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AudioFunctions : MonoBehaviour
{
    //https://forum.unity.com/threads/record-microphone-to-file.415078/
    //https://support.unity3d.com/hc/en-us/articles/206485253-How-do-I-get-Unity-to-playback-a-Microphone-input-in-real-time-
    //int isRecording = 0;
    bool isRecording = false;
    private AudioSource audioSource;

    //private Touch theTouch;
    //private Vector2 touchStartPosition, touchEndPosition;
   
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
       // int length = 44100;
       // float[] clipData = new float[length];
       // audioSource.clip.GetData(clipData, 0);
       // tempRecording.AddRange(clipData);
    }
    public void StartRecording()
    {
        //isRecording = 2;
        Debug.Log("Start rec pressed");
    }

    public void StopRecording()
    {
        //isRecording = 1;
        Debug.Log("Stop rec pressed");
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
        if (Input.GetKeyDown("space"))
        {
            // theTouch = Input.GetTouch(0);

            // if (theTouch.phase == TouchPhase.Began || theTouch.phase == TouchPhase.Ended)
            //{
            isRecording = !isRecording;
            Debug.Log(isRecording == true ? "Is Recording" : "Off");
            //}


            if (isRecording == false)
            {
                //isRecording = 0;
                //stop recording, get length, create a new array of samples
                int lengthRec = Microphone.GetPosition(null);

                Microphone.End(null);
                float[] clipData = new float[lengthRec];
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
                Debug.Log("in record stop mode" + "clip length is: " + lengthRec);

            }
            if (isRecording == true)
            //else
            {
                //isRecording = 0;
                //stop audio playback and start new recording...
                audioSource.Stop();
                tempRecording.Clear();
                Microphone.End(null);
                audioSource.clip = Microphone.Start(null, true, 1, 44100);
                Invoke("ResizeRecording", 1);
                Debug.Log("in record rutine");
            }
        }


        
        //use number keys to switch between recorded clips, start from 1!!
        for (int i = 0; i < 10; i++)
        {
            if (Input.GetKeyDown("" + i))
            {
                SwitchClips(i - 1);
            }
        }
    }
    public void ButtonPressed()
    {
        Debug.Log("pressed sound play");
    }


    //chooose which clip to play based on number key..
    void SwitchClips(int index)
        {
            if (index < recordedClips.Count)
            {
                audioSource.Stop();
                int lengthPlay = recordedClips[index].Length;
                audioSource.clip = AudioClip.Create("recorded samples", lengthPlay, 1, 44100, false);
                audioSource.clip.SetData(recordedClips[index], 0);
                audioSource.loop = true;
                audioSource.Play();
                Debug.Log("play sound");
            }
        }
    


}
