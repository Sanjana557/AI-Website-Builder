export default function StepOne({ formData, setFormData, next }) {
  return (
    <div>
      <h3>Select Website Type</h3>
      <select
  value={formData.website_type}
  onChange={(e) =>
    setFormData({ ...formData, website_type: e.target.value })
  }
  style={{
    width: "100%",
    padding: "12px 16px",
    borderRadius: "12px",
    border: "none",
    background: "rgba(255,255,255,0.15)",
    color: "white",
    fontSize: "16px",
    marginTop: "10px",
    outline: "none"
  }}
>
  <option style={{ color: "black" }}>Portfolio</option>
  <option style={{ color: "black" }}>Business</option>
  <option style={{ color: "black" }}>E-commerce</option>
</select>

      <br /><br />
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
  onClick={next}
>
  Next
</button>

    </div>
  );
}
