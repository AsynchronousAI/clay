import styled from 'styled-components';
import { Heart } from 'react-feather';
import Typography from '@/components/common/Typography';
import { Grid, GridItem, Section, Stack } from '@/components/common/layout';
import TwitterSvg from '@/assets/twitter-icon.svg'
import DiscordSvg from '@/assets/discord-icon.svg'
import GitHubSvg from '@/assets/github-icon.svg'
import links from '@/data/links';

const TwitterIcon = styled(TwitterSvg)`
  width: 48px;
  height: 48px;
`
const DiscordIcon = styled(DiscordSvg)`
  width: 48px;
  height: 48px;
`
const GitHubIcon = styled(GitHubSvg)`
  width: 48px;
  height: 48px;
`

const SocialSection = () => {
  return (
    <Section contained gutterY>
      <Grid columns={{ xs: 1, md: 2, lg: 4}} gap>
        <GridItem>
          <Stack gap={1} align="center" style={{ textAlign: 'center' }}>
            <TwitterIcon />
            <Typography variant="headline-body">Keep up to date</Typography>
            <Typography variant="body-reduced">
              Stay in the know! Follow us @AsynchronousAI on Twitter to get the
              latest updates.
            </Typography>
            <Typography variant="body-reduced"><a href={links.twitter}>Follow Us</a></Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack gap={1} align="center" style={{ textAlign: 'center' }}>
            <DiscordIcon />
            <Typography variant="headline-body">Join the conversation</Typography>
            <Typography variant="body-reduced">
              Some of the best ideas come from our community. Join us to influence clay.
            </Typography>
            <Typography variant="body-reduced"><a href={links.discord}>Start a conversation</a></Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack gap={1} align="center" style={{ textAlign: 'center' }}>
            <GitHubIcon />
            <Typography variant="headline-body">Start Contributing</Typography>
            <Typography variant="body-reduced">
              Help shape the future of clay. Submit an issue or become a contributor today.
            </Typography>
            <Typography variant="body-reduced"><a href={links.githubRepo}>Check it out</a></Typography>
          </Stack>
        </GridItem>
        <GridItem>
          <Stack gap={1} align="center" style={{ textAlign: 'center' }}>
            <Heart size={48} />
            <Typography variant="headline-body">Become a Sponsor</Typography>
            <Typography variant="body-reduced">
              Don&apos;t have time to contribute? You can show your support by becoming a sponsor.
            </Typography>
            <Typography variant="body-reduced"><a href={links.githubSponsor}>Sponsor the Project</a></Typography>
          </Stack>
        </GridItem>
      </Grid>
    </Section>
  );
}

export default SocialSection;
