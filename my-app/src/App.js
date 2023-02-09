import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import axios from 'axios';
import logo from '../src/logo512.png';
import Swal from 'sweetalert2';


function App() {
  const { register, handleSubmit } = useForm();
  const [data, setData] = useState("");
  const [mail, setMail] = useState("");
  const [password, setPassword] = useState("");

  const postData = async () => {
    const test = await axios.get(`http://127.0.0.1:5000/password/?psw=${password}&mail=${mail}`);
    Swal.fire({
      title: test.data,
      onBeforeOpen: () => {
        Swal.showLoading()
      }
    })
  };

  function handleReset(event) {
    event.preventDefault();
    setMail("");
    setPassword("");
  }

  const handleValidate = async () => {
    console.log("test");
    const test = await axios.get(`http://127.0.0.1:5000/connection/?psw=${password}&mail=${mail}`);
    Swal.fire({
      title: test.data,
      onBeforeOpen: () => {
        Swal.showLoading()
      }
    })
  }

  function handleAddAccount(event) {
    event.preventDefault();
    // Code pour le bouton Ajouter Compte
    console.log("Mail : ", mail);
    console.log("Password : ", password);
  }

  return (
    <div className="formCenter">
      <form>
        <img src={logo} alt="" />
        <input
          {...register("Mail")}
          placeholder="Mail"
          value={mail}
          onChange={e => setMail(e.target.value)}
        />
        <input
          {...register("Password")}
          placeholder="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <p>{data}</p>
        <div className="ButtonGroup">
          <input type="button" value="Reset" onClick={handleReset} />
          <input type="button" value="Valider" onClick={handleValidate} />
          <input type="button" value="Ajouter Compte" onClick={postData} />
        </div>
      </form>
    </div>
  );
}

export default App;
