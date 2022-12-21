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
      {"\n"}

        <ul>Language support for:</ul>
{"\n"}
        <li>JavaScript, TypeScript (and other varients)</li>
{"\n"}
        <li>Python</li>
{"\n"}
        <li>Java</li>
{"\n"}
        <li>Go</li>
{"\n"}
        <li>Rust</li>
{"\n"}
        <li>PHP</li>
{"\n"}
        <li>Lua</li>
{"\n"}
        <li>Swift</li>
{"\n"}
        <li>Scala</li>
{"\n"}
        <li>Julia</li>
{"\n"}
        <li>Perl</li>
{"\n"}
        <li>and more...</li>
{"\n"}
        <ul>Added utility belts:</ul>
{"\n"}
        <li>app</li>
{"\n"}
        <li>cli</li>
{"\n"}
        <li>web</li>
{"\n"}
        <li>game</li>
{"\n"}
        <li>function</li>
{"\n"}
        <ul>Package managers:</ul>
{"\n"}
        <li>npm</li>
{"\n"}
        <li>pip</li>
{"\n"}
        <li>go</li>
{"\n"}
        <li>cargo</li>
{"\n"}
        <li>lua rocks</li>
{"\n"}
      </Section>

    </div>
  );
}
