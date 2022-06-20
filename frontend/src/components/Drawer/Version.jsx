import {Drawer} from "antd";
import Markdown from "@/components/CodeEditor/Markdown";

const md = ``


export default ({visible, setVisible}) => {
  return (
    <Drawer visible={visible} onClose={() => setVisible(false)} width={500}>
      <Markdown value={md}/>
    </Drawer>
  )
}
