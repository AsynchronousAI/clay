import { Section } from '@/components/common/layout';
import Typography from '@/components/common/Typography';

export default function DevPage() {
  return (
    <Section contained gutterY>
      <Typography variant="headline">Clay Extensions</Typography>

      <Typography variant="headline-reduced">VSCode</Typography>
      The Clay Extension for VSCode supports the clay versions of the languages, Give you a GUI based experience for creating clay projects and more. The extension is currently in beta and is not available for public use.
      
      <Typography variant="headline-reduced">Store</Typography>
      <ul>
      <a>Clay Mobile App Utility</a>

      This extension adds a mobile utility belt which allows you to make mobile apps easily

      ```bash
      clay install mobile
      ```
      </ul>
      <ul>
      <a>Clay Words Utility</a>

      This extension adds a words utility belt which allows you to make word based apps easily.

      This extension includes a word database with over 100,000 words.

      ```bash
      clay install words
      ```
      
      ```lua
      print(utilities.words.random())
      ```
      </ul>
    </Section>
  );
}
