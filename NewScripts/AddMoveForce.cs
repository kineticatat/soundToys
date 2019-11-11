using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AddMoveForce : MonoBehaviour
{
    private Rigidbody myMarble;

    // Start is called before the first frame update
    void Start()
    {
        myMarble = GetComponent<Rigidbody>();
        
    }

    // Update is called once per frame
    void Update()
    {
        //float moveHorizontal = Input.GetAxis("Horizontal");
        float moveHorizontal = Input.acceleration.x;
        //float moveVertical = Input.GetAxis("Vertical");
        float moveVertical = Input.acceleration.y;

        Vector3 movement = new Vector3(moveHorizontal * 2, 0.0f, moveVertical * 2);

        myMarble.AddForce(movement);

    }
}
