export default function StepThree({ generate }) {
  return (
    <div>
      <h3>Generate Website</h3>

      <button
        style={{
          marginTop:"20px",
          padding:"10px 25px",
          borderRadius:"20px",
          border:"none",
          background:"#38bdf8",
          color:"black",
          fontWeight:"bold",
          cursor:"pointer"
        }}
        onClick={generate}
      >
        Generate
      </button>
    </div>
  );
}
