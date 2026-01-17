import { useState } from "react";
import StepOne from "./components/StepOne";
import StepTwo from "./components/stepTwo";
import StepThree from "./components/StepThree";
import Preview from "./components/Preview";
import { generateWebsite } from "./api";

export default function App() {
  const [step, setStep] = useState(1);
  const [html, setHtml] = useState("");
  const [formData, setFormData] = useState({
    website_type: "Portfolio",
    tone: "Modern",
    color: "Dark",
    sections: ["Hero", "Gallery", "Contact"],
  });

  const generate = async () => {
    const result = await generateWebsite(formData);
    setHtml(result.html);
  };

 return (
  <div style={{
    minHeight: "100vh",
    background: "linear-gradient(135deg,#0b1020,#1b2a4e,#312e81)",
    color: "white",
    padding: "40px"
  }}>

    <div style={{
      maxWidth: "900px",
      margin: "auto",
      background: "rgba(255,255,255,0.08)",
      borderRadius: "20px",
      padding: "30px",
      boxShadow: "0 20px 40px rgba(0,0,0,0.5)"
    }}>

      <h1 style={{color:"#a5b4fc", textAlign:"center"}}>AI Website Builder</h1>
      <p style={{textAlign:"center", opacity:0.8}}>
        Design professional websites using AI
      </p>

      {step === 1 && <StepOne formData={formData} setFormData={setFormData} next={() => setStep(2)} />}
      {step === 2 && <StepTwo formData={formData} setFormData={setFormData} next={() => setStep(3)} />}
      {step === 3 && <StepThree generate={generate} />}

      <Preview html={html} />
    </div>
  </div>
);
}
