import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import axios from 'axios';

function App() {
  const { register, handleSubmit } = useForm();
  const [data, setData] = useState("");

  const postData = async (password) => {
    console.log("test");
    const response = await axios.get('http://localhost:5000/test',
      {
        headers: {
          // remove headers
        }
      });
    console.log(response.data);
  };

  // async () => {$

  // try {
  //   const res = await fetch("http://localhost:5000/test");
  //   const response = await res.text();
  //   console.log(response);
  // } catch (error) {
  //   console.error(error);
  // }
  // };

  return (
    <form onSubmit={test()} >
      <input {...register("Mail")} placeholder="Mail" />
      <input {...register("Password")} placeholder="password" />
      <p>{data}</p>
      <input type="submit" />
    </form>
  );
}

export default App;
