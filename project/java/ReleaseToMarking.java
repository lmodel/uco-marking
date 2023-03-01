package None;

import java.util.List;
import lombok.*;



/* version: 1.1.0 */


/**
  A release-to marking is a grouping of characteristics unique to the expression of data MarkingDefinitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey details of authorized persons and/or organizations to which to the associated content may be released. The existence of the Release-To marking restricts access to ONLY those identities explicitly listed, regardless of whether another data marking exists that allows sharing with other members of the community.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ReleaseToMarking extends MarkingModel {

  private List<String> authorizedIdentities;
  private List<String> definitionType;

}