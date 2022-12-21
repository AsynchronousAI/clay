import styled from 'styled-components';
import { Section } from '@/components/common/layout';
import Typography from '@/components/common/Typography';

const HeroSection = styled(Section)`
  text-align: center;
`;
const HeroIntro = styled(Typography)`
  width: 75%;
  margin: 0 auto;
  margin-top: 20px;
`;

export default function WhatsNewPage() {
  return (
    <div>
      <HeroSection contained gutterY>
        <Typography variant="headline" as="h1">
          What’s included in clay
        </Typography>
        <HeroIntro variant="intro">
          Learn about the key features available in clay, the code editor
          for building anything in any language.
        </HeroIntro>
      </HeroSection>
      <Section contained gutterBottom>
        <Typography variant="headline-reduced">clay 0.1</Typography>
        Beta release of clay. Currently not available for download but you can visit the <a href={"https://example.com"}>online playground</a>.
        <ul>Language support for:</ul>
        <li>JavaScript, TypeScript (and other varients)</li>
        <li>Python</li>
        <li>Java</li>
        <li>Go</li>
        <li>Rust</li>
        <li>PHP</li>
        <li>Lua</li>
        <li>Swift</li>
        <li>Scala</li>
        <li>Julia</li>
        <li>Perl</li>
        <li>and more...</li>
        <ul>Added utility belts:</ul>
        <li>app</li>
        <li>cli</li>
        <li>web</li>
        <li>game</li>
        <li>function</li>
        <ul>Package managers:</ul>
        <li>npm</li>
        <li>pip</li>
        <li>go</li>
        <li>cargo</li>
        <li>lua rocks</li>
      </Section>
    </div>
  );
}
