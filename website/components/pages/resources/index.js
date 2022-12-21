import { Section } from '@/components/common/layout';
import Typography from '@/components/common/Typography';
export default function ResourcesPage() {
  return (
    <Section contained gutterY>
       <Typography variant="headline">Resources</Typography>
        <Typography variant="headline-reduced">API</Typography>
        The Clay API allows you to use the Clay CLI online for enviorments that do not support the CLI. The API is currently in beta and is not available for public use.
        <Typography variant="headline-reduced">CLI</Typography>
        The Clay CLI is a command line interface for the Clay API. The CLI is currently in beta and is not available for public use. 
        <Typography variant="headline-reduced">Extensions</Typography>
        The Clay Extension for VSCode supports the clay versions of the languages, Give you a GUI based experience for creating clay projects and more. The extension is currently in beta and is not available for public use.
        <Typography variant="headline-reduced">Playground</Typography>
        The Clay Playground is a web based version of the Clay API made for testing. You can visit it <a href={"https://example.com"}>here</a>.
 

    </Section>
  );
}
