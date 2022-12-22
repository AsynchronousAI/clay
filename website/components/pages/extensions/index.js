import { Section } from '@/components/common/layout';
import Typography from '@/components/common/Typography';

export default function DevPage() {
  return (
    <Section contained gutterY>
      <Typography variant="headline">Clay Extensions</Typography>
{"\n"}
    <Section contained gutterTop={i === 0} gutterBottom key={variant}>
          <Typography variant="eyebrow-super">VSCode</Typography>
      The Clay Extension for VSCode supports the clay versions of the languages, Give you a GUI based experience for creating clay projects and more. The extension is currently in beta and is not available for public use.
       </Section>  
        <Section contained gutterTop={i === 0} gutterBottom key={variant}>
      <Typography variant="eyebrow-super">Store</Typography>
      <ul>
      <a>Clay Mobile App Utility</a>
{"\n"}
      This extension adds a mobile utility belt which allows you to make mobile apps easily
{"\n"}
      ```bash
      clay install mobile
      ```
      </ul>
      <ul>
      <a>Clay Words Utility</a>
{"\n"}
      This extension adds a words utility belt which allows you to make word based apps easily.
{"\n"}
      This extension includes a word database with over 100,000 words.
{"\n"}
      ```bash
      clay install words
      ```
{"\n"}
      ```lua
      print(utilities.words.random())
      ```
      </ul>
      </Section>
    </Section>
  );
}
