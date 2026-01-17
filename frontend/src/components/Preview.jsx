export default function Preview({ html }) {
  if (!html) return null;
  return (
    <iframe
      title="preview"
      srcDoc={html}
      style={{ width: "100%", height: "500px", border: "1px solid #ccc" }}
    />
  );
}
